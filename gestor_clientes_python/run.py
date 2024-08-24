"""LA APP SE EJECUTARÁ A TRAVÉS DE ESTE FILE"""


"""

Ejecución Alternativa:

El script puede ejecutar dos modos diferentes dependiendo del argumento de la línea de comandos.
- Modo -t (python3 run.py -t): Si se pasa el argumento -t, se llama a la función iniciar del módulo menu. Esta función inicia una interfaz o funcionalidad diferente.
- Modo Normal (python3 run.py ): Si no se pasa el argumento -t, se inicia la interfaz gráfica de usuario principal (MainWindow) definida en el módulo ui.

"""

import sys
import ui
import menu 


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1]=="-t":
        menu.iniciar()
    else:
        app=ui.MainWindow()
        app.mainloop()