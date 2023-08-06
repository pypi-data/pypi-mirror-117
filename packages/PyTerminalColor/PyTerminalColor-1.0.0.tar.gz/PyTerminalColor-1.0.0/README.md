# PyTerminalColor
 Create attractive python progams with foreground, background colors and styles.
 

##

## Installation

### Using PyPi

  - with pip
    ```
    pip install PyTerminalColor
    ```
  
  
### Using git

  - clone repo
     ```
     git clone https://github.com/dmdhrumilmistry/PyTerminalColor.git
     ```
   
  - Change to PyTerminalColor repo directory
     ```
     cd PyTerminalColor
     ```
   
  - install PyTerminalColor
     ```
     pip install -e .
     ```
     
### Verify installation

 ```
 python -m PyTerminalColor
 ```
     
##
### Features

   - `Foreground Colors`: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, LIGHT_GRAY, CYAN
   - `Background Colors`: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, LIGHT_GRAY, CYAN
   - `Styles`: NORMAL, BOLD, ITALIC, UNDERLINE

##
## Usage
- Import and create an TerminalColor object.
 ```python 
 from PyTerminalColor.TerminalColor import TerminalColor
 
 
 colorize = TerminalColor(fgcolor='YELLOW', bgcolor='RED', style='BOLD')
 ```
 
- print colored text with default object values
```python
colorize.cprint('TerminalColor')
```

- print colored text with other values
 ```python
 colorize.cprint('TerminalColor',use_default=False, fgcolor='YELLOW', bgcolor='BLACK', style='ITALIC')
 ```
 
 > cprint default values:
  > ```python
  > use_default = True
  > fgcolor = 'LIGHT_GRAY'
  > bgcolor = 'BLACK'
  > style = 'NORMAL'
  > ```
 
<!-- ![Output]() -->


##
## [License](https://github.com/dmdhrumilmistry/PyTerminalColor/blob/main/LICENSE)
  **MIT License**
  
  
##
### Have any Issues?
Create an issue from ***[Issues Tab](https://github.com/dmdhrumilmistry/PyTerminalColor/issues)***

  
##
## Leave A Star⭐

  
### Connect With Me on:
  
  <p align ="left">
    <a href = "https://github.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Github-dmdhrumilmistry-333"></a>
    <a href = "https://www.instagram.com/dmdhrumilmistry/" target="_blank"><img src = "https://img.shields.io/badge/Instagram-dmdhrumilmistry-833ab4"></a>
    <a href = "https://twitter.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Twitter-dmdhrumilmistry-4078c0"></a><br>
    <a href = "https://www.youtube.com/channel/UChbjrRvbzgY3BIomUI55XDQ" target="_blank"><img src = "https://img.shields.io/badge/YouTube-Dhrumil%20Mistry-critical"></a>
    <a href = "https://dhrumilmistrywrites.blogspot.com/" target="_blank"><img src = "https://img.shields.io/badge/Blog-Dhrumil%20Mistry-bd2c00"></a>
    <a href = "https://www.linkedin.com/in/dhrumil-mistry-312966192/" target="_blank"><img src = "https://img.shields.io/badge/LinkedIn-Dhrumil%20Mistry-4078c0"></a><br>
   </p>
  

