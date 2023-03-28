Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> descuento_retencion = sueldo * 0.3
...     descuento_ISSS = sueldo * ISSS
...     descuento_AFP = sueldo * AFP
...     total_descuentos = descuento_ISSS + descuento_AFP + descuento_retencion
...     sueldo_neto = sueldo - total_descuentos
...     
...     return [descuento_retencion, descuento_ISSS, descuento_AFP, total_descuentos, sueldo_neto]
... sueldo = float(input('Ingrese el sueldo: '))
... try:
...     descuentos = calcular_descuentos(sueldo)
...     tabla = pd.DataFrame({
...         'Sueldo': [sueldo],
...         'Retención': [descuentos[0]],
...         'Sueldo - ISSS': [descuentos[1]],
...         'Sueldo - AFP': [descuentos[2]],
...         'Total del descuento': [descuentos[3]],
...         'Total del sueldo': [descuentos[4]],
...     })
... 
