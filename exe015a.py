#desafio011
larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
área = larg*alt
tinta = área / 2
print('Sua parede tem a dimensão {}x{} e sua área é de {:.2}m².'.format(larg,alt,área))
print('Para pintar a área dessa parede você precisará de {}l de tinta.'.format(tinta))
