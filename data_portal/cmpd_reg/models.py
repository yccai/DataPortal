from __future__ import unicode_literals
from django.db import models
from django_rdkit import models as rdkit_models


class Fingerprint(rdkit_models.Model):

	bfp = rdkit_models.BfpField(null=True,
								verbose_name="Binary Fingerprint")
	class Meta:
		db_table = 'compound_fingerprint'
		verbose_name = 'Compound Fingerprint'
		verbose_name_plural = 'Compound Fingerprints'

	def __unicode__(self):
		return u"Compound Fingerprint with ID {}".format(self.id)

class Property(models.Model):

	amw = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=3,
								verbose_name="Average Molecular Weight")
	hbd = models.PositiveSmallIntegerField(blank=True, null=True, 
											verbose_name="Hydrogen Bond Donors")
	hba = models.PositiveSmallIntegerField(blank=True, null=True,
											verbose_name="Hydrogen Bond Acceptors")
	tpsa = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=3,
								verbose_name="Total Polar Surface Area")

	class Meta:
		db_table = 'compound_property'
		verbose_name = 'Compound Property'
		verbose_name_plural = 'Compound Properties'

	def __unicode__(self):
		return u"Compound Property with ID {}".format(self.id)


class Compound(rdkit_models.Model):

	smiles = models.CharField(max_length=2048)
	molecule = rdkit_models.MolField(null=False)
	inchi = models.CharField(max_length=2048, blank=True, null=True)
	inchi_key = models.CharField(max_length=2048, blank=True, null=True)
	ctab = models.TextField(blank=True, null=True)
	datetime_loaded = models.DateTimeField(auto_now_add=True,
                                     		verbose_name="Datetime When Compound Registered")

	fingerprint = models.OneToOneField(Fingerprint,
									   blank=True,
                                       null=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name="Compound Fingerprint")

	property = models.OneToOneField(Property,
									blank=True,
									null=True,
									on_delete=models.SET_NULL,
									verbose_name="Compound Property")

	class Meta:
		db_table = 'compound'
        verbose_name = "Compound"
        verbose_name_plural = "Compounds"

	def __unicode__(self):
		return u"Compound ID {id} loaded on {date}".format(id=self.id, date=self.datetime_loaded.strftime('%-I:%M %p %B %-d %Y'))
