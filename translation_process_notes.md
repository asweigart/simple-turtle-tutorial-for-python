Translation Process Notes

Here's a few notes when translating the English STT to another language.

NOTE: Before the table of contents, add this part to be translated:

    This tutorial was originally written in English and translated to LANGUAGE. The external links are to English language resources. If you have corrections for this tutorial, please email [al@inventwithpython.com](mailto:al@inventwithpython.com).



NOTE: At the end of the introduction, add this part:

    **Note for non-English versions of this tutorial:** The Python programming language comes with the turtle package. However, the code in the turtle package is in English. The tortuga package provides translated code in several languages. To install the tortuga package, run the following code from the Python interactive shell, also called the REPL. The interactive shell has the prompt `>>>` or the prompt `In [1]:`.

    ```python
    import sys, subprocess; subprocess.run([sys.executable, '-m', 'pip', 'install', 'tortuga'])
    ```

    To check if tortuga installed successfully, run the following code from the interactive shell:

    ```python
    from tortuga import *
    ```

    If nothing appears, then tortuga installed successfully.

    The Python programming langauge's keywords and error messages are still in English. You can use [https://translate.google.com/](https://translate.google.com/) to translate these. The original English version of this tutorial is at [https://inventwithpython.com/stt/](https://inventwithpython.com/stt/)


NOTE: Find the "ModuleNotFoundError" and change some of the error message text that is in English.

NOTE: You will need a new screenshot of orig_screenshot_write_hello.webp. Make the new filename like orig_screenshot_write_hello_ES.webp.

NOTE: Update the arguments here: The style argument can either be `'normal'`, `'bold'`, `'italic'`, `'underline'`, or any combination of those words like `'bold italic'`.

NOTE: Make sure all the filenames are translated.

