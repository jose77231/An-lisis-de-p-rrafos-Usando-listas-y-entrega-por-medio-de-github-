cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi mattis lacus vehicula eros lacinia, nec auctor tellus porttitor. Quisque semper eget erat vitae faucibus. Donec ornare sapien id urna pretium blandit. Suspendisse potenti. Integer sodales facilisis ultricies. Phasellus pretium vehicula odio nec viverra. Etiam nunc enim, eleifend consectetur laoreet quis, sodales ut dolor. Sed nulla dolor, sollicitudin at pharetra vitae, pellentesque non elit. Pellentesque ut ex vitae dolor tincidunt porttitor. Cras vitae odio ac augue iaculis gravida. Mauris sit amet consectetur ligula. Suspendisse nec ornare risus, id viverra augue.

Nullam nec massa cursus, posuere purus sed, pharetra elit. Nulla eleifend vitae massa nec semper. Sed vitae sem sed velit consectetur congue. Cras ultrices odio in tempus condimentum. Maecenas congue semper massa viverra sodales. Nullam at nibh a nulla venenatis dictum. Curabitur at ligula et lectus tristique accumsan. Suspendisse sapien tellus, pharetra ut convallis sit amet, efficitur non leo. Suspendisse laoreet cursus nisl egestas aliquam. Integer mi orci, interdum sit amet lobortis sed, efficitur id mi. Proin placerat nisi at elit blandit, pellentesque dignissim magna finibus. Pellentesque vestibulum, velit vitae bibendum viverra, leo lacus finibus tellus, et ornare dui ante et ex. Praesent auctor ornare neque sit amet porttitor. Nulla arcu massa, egestas eu metus eu, varius iaculis nibh.

Proin tempus pretium auctor. Sed at augue ullamcorper, efficitur nibh sit amet, aliquet arcu. Nullam eu sagittis metus. Phasellus velit lacus, tincidunt eu congue a, tempor venenatis nulla. Nunc sagittis massa lobortis odio imperdiet dictum. Proin iaculis, elit quis gravida vehicula, orci sem tincidunt libero, dictum sodales odio nulla id lacus. Vestibulum egestas pulvinar commodo. Nullam lacinia erat molestie fringilla interdum. Ut tempor ante augue, malesuada imperdiet ipsum gravida accumsan. Nam sagittis velit diam, id luctus enim gravida in. Mauris non nisl hendrerit, venenatis lorem nec, aliquam tortor. Curabitur hendrerit lorem diam, ut dapibus lacus feugiat eget. Fusce varius, tortor ut efficitur sodales, erat mi cursus orci, at sollicitudin risus nulla rutrum felis. Mauris vel ipsum dolor.

Pellentesque tristique est vel blandit porttitor. Integer finibus placerat felis, at dignissim elit sagittis posuere. Sed laoreet bibendum consequat. Aenean ullamcorper eleifend turpis a ultrices. Phasellus rhoncus felis ac condimentum fermentum. Nam sollicitudin, risus vitae vestibulum aliquet, augue massa placerat felis, at aliquet mauris lorem a lorem. Duis id pulvinar est. Quisque tincidunt, lacus aliquet suscipit lobortis, metus metus scelerisque dui, et feugiat ex magna et mauris. Etiam ut ante enim. Integer varius rutrum sem. Praesent quam mauris, imperdiet bibendum fermentum id, tincidunt at purus.

Vestibulum eget nisi sit amet ligula pellentesque fringilla. Aliquam malesuada ut purus nec posuere. Pellentesque leo ante, interdum vel porttitor eget, ultricies vitae ex. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent tempus quam vel turpis hendrerit mattis. Phasellus sagittis libero lorem, eget interdum libero venenatis vel. In vitae nunc est. Etiam sit amet dignissim ex, eu tempor eros. Sed ut eros leo.
"""

letras = 'abcdefghijklmnñopqrstuvwxyz'
caracteres =['a','e','i', 'o','u', ' ', ',','.' ]
estadisticas = ['Total de caracteres:', 'Total de letras : ', 'Total de vocales a :', 'Total de vocales e :', 'Total de vocales i :', 'Total de vocales o :', 'Total de vocales u :', 'Total de espacios :', 'Total de comas:', 'Total de puntos:']
totales = [0] * len(estadisticas)

for char in cadenaLarga:
    totales[0] += 1  # Total de caracteres
    if char in letras:
        totales[1] += 1  # Total de letras
    if char in caracteres[0]:
        totales[2] += 1  # Total de vocales a
    elif char in caracteres[1]:
        totales[3] += 1  # Total de vocales e
    elif char in caracteres[2]:
        totales[4] += 1  # Total de vocales i
    elif char in caracteres[3]:
        totales[5] += 1  # Total de vocales o
    elif char in caracteres[4]:
        totales[6] += 1  # Total de vocales u
    elif char == ' ':
        totales[7] += 1  # Total de espacios
    elif char == ',':
        totales[8] += 1  # Total de comas
    elif char == '.':
        totales[9] += 1  # Total de puntos

print("Resumen de estadísticas:")
for i in range(len(estadisticas)):
    print(estadisticas[i], totales[i])