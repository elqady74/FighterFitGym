from django.db import models

class GymUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=[('trainee', 'Trainee'), ('trainer', 'Trainer'), ('admin', 'Admin')])
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"

    class Meta:
        db_table = 'gym_user'

class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(GymUser, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    auto_renew = models.BooleanField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Membership {self.membership_type} for {self.user.fname}"

    class Meta:
        db_table = 'membership'

class Trainer(models.Model):
    trainer_id = models.OneToOneField(GymUser, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    certification = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Trainer: {self.trainer_id.fname} {self.trainer_id.lname}"

    class Meta:
        db_table = 'trainer'

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_type = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_participants = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Session {self.session_type} at {self.start_time}"

    class Meta:
        db_table = 'session'

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(GymUser, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Booking for {self.user.fname} in {self.session.session_type}"

    class Meta:
        db_table = 'booking'

class Conducts(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'conducts'
        unique_together = ('trainer', 'session')

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(GymUser, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField()
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.transaction_id} by {self.user.fname}"

    class Meta:
        db_table = 'payment'

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(GymUser, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True, blank=True)
    method = models.CharField(max_length=50)

    def __str__(self):
        return f"Attendance for {self.user.fname} at {self.check_in_time}"

    class Meta:
        db_table = 'attendance'

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(GymUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_type = models.CharField(max_length=50)
    sent_at = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Notification {self.title} for {self.user.fname}"

    class Meta:
        db_table = 'notification'

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    purchase_date = models.DateField()
    last_maintenance = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Equipment: {self.name}"

    class Meta:
        db_table = 'equipment'