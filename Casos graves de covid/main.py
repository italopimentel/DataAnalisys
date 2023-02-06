from matplotlib import pyplot
import pandas as pd
from scipy import stats

data = pd.read_csv('casosgravescovid.csv', sep=';', on_bad_lines='skip')

data.dropna(subset='idade', inplace=False)

mortes_masculinas_idade = data[data['sexo'] == 'Masculino']['idade']
mortes_femininas_idade= data[data['sexo'] == 'Feminino']['idade']

sampleMasc = pd.to_numeric(mortes_masculinas_idade, errors='coerce')
sampleFem = pd.to_numeric(mortes_femininas_idade, errors='coerce')

t_start, p_value = stats.ttest_ind(sampleMasc, sampleFem, equal_var= False)

medianaMasc = sampleMasc.median()
medianaFem = sampleFem.median()

mediaMasc = sampleMasc.mean()
mediaFem = sampleFem.mean()

print(t_start)
print(p_value)

print(mediaMasc)
print(mediaFem)

