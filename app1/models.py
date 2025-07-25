from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15)
    Employee_Id = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='Employees/')
    authorized = models.BooleanField(default=False)

    def __str__(self):
        return self.Employee_Id

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    extra_time = models.DurationField(default=timedelta(0))  # Time outside office
    last_action_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.Employee_Id} - {self.date}"

    def mark_checked_in(self):
        now = timezone.now()
        if self.check_in_time and self.check_out_time:
            extra_time_spent = now - self.check_out_time
            self.extra_time += extra_time_spent
            self.check_out_time = None
        elif not self.check_in_time:
            self.check_in_time = now
        self.last_action_time = now
        self.save()

    def mark_checked_out(self):
        now = timezone.now()
        if self.check_in_time and not self.check_out_time:
            self.check_out_time = now
            self.last_action_time = now
            self.save()
        else:
            raise ValueError("Cannot mark check-out without check-in.")

    def calculate_duration(self):
        if self.check_in_time and self.check_out_time:
            total = self.check_out_time - self.check_in_time
            adjusted = total - self.extra_time
            return adjusted if adjusted.total_seconds() > 0 else timedelta(0)
        return None

    def formatted_duration(self):
        duration = self.calculate_duration()
        if duration:
            total_seconds = int(duration.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        return "Not Checked Out"

    def get_office_time(self):
        now = timezone.now()
        if not self.check_in_time:
            return timedelta(0)
        if self.check_out_time:
            total_time = self.check_out_time - self.check_in_time
        else:
            total_time = now - self.check_in_time

        office_time = total_time - self.extra_time
        if office_time.total_seconds() < 0:
            return timedelta(0)
        return office_time

    def formatted_office_time(self):
        office_time = self.get_office_time()
        total_seconds = int(office_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def attendance_status(self):
        """Return attendance status based on office time."""
        office_time = self.get_office_time()
        total_hours = office_time.total_seconds() / 3600

        if total_hours < 2:
            return "None"
        elif 2 <= total_hours < 4:
            return "Half"
        elif 4 <= total_hours < 7:
            return "Full"
        else:
            return "Overtime"

    def get_overtime_duration(self):
        """Return how much overtime if more than 7 hours, else None."""
        office_time = self.get_office_time()
        if office_time.total_seconds() / 3600 > 7:
            overtime = office_time - timedelta(hours=7)
            total_seconds = int(overtime.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        return None

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date = timezone.now().date()
        super().save(*args, **kwargs)

class AttendanceLog(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=10, choices=[('checkin', 'Check In'), ('checkout', 'Check Out')])

    def __str__(self):
        return f"{self.attendance.employee.Employee_Id} - {self.action} at {self.timestamp.strftime('%H:%M:%S')}"

class CameraConfiguration(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Give a name to this camera configuration")
    camera_source = models.CharField(max_length=255, help_text="Camera index (0 for default webcam or RTSP/HTTP URL for IP camera)")
    threshold = models.FloatField(default=0.6, help_text="Face recognition confidence threshold")

    def __str__(self):
        return self.name
