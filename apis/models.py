from django.db import models


class Profile(models.Model):
  token = models.CharField(max_length=700)
  token_id = models.CharField(max_length=700, null=True, blank=False)
  host_name = models.CharField(max_length=700)
  os_name = models.CharField(max_length=700)
  os_version = models.CharField(max_length=700)
  os_manufacturer = models.CharField(max_length=700)
  os_configuration = models.CharField(max_length=700)
  os_build_type = models.CharField(max_length=700)
  registered_owner = models.CharField(max_length=700)
  registered_organization = models.CharField(max_length=700)
  product_iD = models.CharField(max_length=700)
  original_Install_Date = models.CharField(max_length=700)
  system_Boot_Time = models.CharField(max_length=700)
  system_Manufacturer = models.CharField(max_length=700)
  system_Model = models.CharField(max_length=700)
  system_Type = models.CharField(max_length=700)
  processor = models.CharField(max_length=700)
  bios_Version = models.CharField(max_length=700)
  windows_Directory = models.CharField(max_length=700)
  system_Directory = models.CharField(max_length=700)
  system_Locale = models.CharField(max_length=700)
  input_Locale = models.CharField(max_length=700)
  time_Zone = models.CharField(max_length=700)
  total_Physical_Memory = models.CharField(max_length=700)
  available_Physical_Memory = models.CharField(max_length=700)
  sender_id = models.URLField(max_length=700)
  decrypted = models.BooleanField(default=False)
  is_verified = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.registered_owner} - {self.system_Model}"

class How_To_Pay(models.Model):
  title = models.CharField(max_length=100, null=True, blank=False, help_text="#step 1")
  description = models.TextField(null=True, blank=False)
  rep = models.CharField(max_length=20, null=True, blank=False, help_text="first", unique=True)
  image = models.ImageField(default='avatar.png', upload_to='how_img/', null=True, blank=False)

  def __str__(self):
    return f"{self.title}, {self.rep}"






  

