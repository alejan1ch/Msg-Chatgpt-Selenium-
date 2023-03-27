WinWait("Abrir") ; wait for the file dialog window to appear
Sleep(200) ; wait for the window to fully load
ControlSetText("Abrir", "", "Edit1", "C:\Users\alcrh\OneDrive - Instituto Tecnológico de Minatitlán\Escritorio\ALE\Alejandro_Cruz_Full_Stack_Python_Developer.pdf") ; set the file path in the file name field
ControlClick("Abrir", "", "Button1") ; click the Open button to upload the file
WinWaitClose("Abrir") ; wait for the file dialog window to close after the file is uploaded
