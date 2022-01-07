# Scripts
Simple scripts for simple things

### Directory Structure:
```
Scripts/
├── README.md
└── Scripts/
    ├── 16BitAlphaNumericStringGen.py
    ├── cost_calc.py
    ├── DirectoryTreePrint/
    │   ├── directory_tree_print.py
    │   └── directory_tree_print_extended.py
    └── keyboardDeactivate/
        ├── keyboard.ico
        ├── keyboardDeactivate.py
        └── ShortCutCreate.py
```
### Scripts:

#### 1. 16 Bit Alpha Numeric String Generator
**<u>Description</u>**: Generates an alphanumeric string (including special characters) of length 15 characters.
* File Name: Scripts/16BitAlphaNumericStringGen.py
* Parameters: None
* Sample Output:
```
QOgiX{,6;+7=RN'
```

#### 2. Cost Calc:
**<u>Description</u>**: Simple script to calculate cost of living for different countries.
* File Name: Scripts/cost_calc.py
* Function Parameter: val(Can be list or int.).
Additional inputs: Asks for currency type and number of semesters.

* Example 1 :
```
conv(1)
1. for EUR
2. for Cad
3. for USD
Input:1
Number of Semester:1
84.32
```

* Example 2:
```
conv([144, 790*6])
1. for EUR
2. for Cad
3. for USD
Input:1
Number of Semester:4
1647275.52
```

#### 3. Directory Tree Print
**<u>Description</u>**: Prints the directory Tree.

1. Version 1:
    * File Name: Scripts/DirectoryTreePrint/directory_tree_print.py  
    * Created By: https://stackoverflow.com/users/1226857/dhobbs
    * Input Parameters: startpath (Path of the root directory from which tree is to be displayed.)
    * Sample Usage:
    ```
    list_files("D:\\Personal\\Git\\Scripts")
    ```
    * Output:
    ```
    Scripts/
    README.md
    Scripts/
        16BitAlphaNumericStringGen.py
        cost_calc.py
        DirectoryTreePrint/
            directory_tree_print.py
            directory_tree_print_extended.py
        keyboardDeactivate/
            keyboard.ico
            keyboardDeactivate.py
            ShortCutCreate.py
    ```
2. Version 2:
    * File Name: Scripts/DirectoryTreePrint/directory_tree_print_extended.py
    * Created By: https://stackoverflow.com/users/2479038/abstrus
    * Sample Usage:
    ```
    paths = DisplayablePath.make_tree(Path(''))
    for path in paths:
        print(path.displayable())
    ```
    * Output:
    ```
    Scripts/
    ├── README.md
    └── Scripts/
        ├── 16BitAlphaNumericStringGen.py
        ├── cost_calc.py
        ├── DirectoryTreePrint/
        │   ├── directory_tree_print.py
        │   └── directory_tree_print_extended.py
        └── keyboardDeactivate/
            ├── keyboard.ico
            ├── keyboardDeactivate.py
            └── ShortCutCreate.py
    ```
#### 4. Keyboard Deactivate
**<u>Description</u>**: Script created when lenovo keyboard was malfunctioning and had to be deactivated. 
    **<u>NOTE</u>**: Was made for arch Linux. 
* Folder Directory: Scripts/keyboardDeactivate
* Contains: An icon for keyboard, Python file for deactivating the keyboard from a list of available keyboard input options and a python file that creates shortcut for the script.
