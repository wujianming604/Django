from django import forms
from .models import SangerSamples, SangerZipFiles

class SangerSamplesForm(forms.ModelForm):
    class Meta:
        model = SangerSamples
        fields = (
            'sampleName', 'chrom', 'pos', 'ref', 'alt',
            'genoType', 'abiFileUrl', 'abiPngUrl'
        )

class SangerZipFilesForm(forms.ModelForm):
    class Meta:
        model = SangerZipFiles
        fields = (
            'fileName', 'sampleNumbers'
        )