## vsml: a (v)ery (s)imple (m)arkup (l)anguage
###### “avoiding complexity reduces bugs.” - linus torvalds
## table of contents
- [features](#features)
  * [current features](#current-features)
  * [planned features](#planned-features)
- [file syntax](#file-syntax)
- [functions](#functions)
  * [initFile](#initFile)
  * [findSecStart](#findSecStart)
  * [findSecEnd](#findSecEnd)
  * [findKey](#findKey)
  * [readKeyValue](#readKeyValue)
  * [editKeyValue](#editKeyValue)
  * [rename](#rename)
  * [add](#add)
  * [delete](#delete)
## features
### current features
- simple ini-like syntax
- lightning fast python functions
- comments
### planned features
- toml-like subsections
- make initFile check for more possible issues
## file syntax
``` ini
# a comment before a section!
[ExampleSection]
ExampleKey1=ExampleValue1
ExampleKey2=ExampleValue2

# a comment between sections!

[ExampleSection2]
# a comment inside a section!
ExampleKey1=ExampleValue1
ExampleKey2=ExampleValue2
ExampleKey3=ExampleValue3
# a comment at the end of the file!
```
## functions
### initFile
the `initFile` function checks if the file exists, and can be written to.

if it is possible to write to the file, it will strip the file of unneeded whitespace so that the following functions will work properly.

in future versions, this function will attempt to fix files with syntax errors.

it is highly recommended to run this function before any others.

usage:
``` python
initFile("/path/to/file.vsml")
```
### findSec
the `findSec` function returns the first line, and last line of a section, in the form of a list.

usage:
``` python
findSec("/path/to/file.vsml", "ExampleSection1") # returned: [ 0, 2 ]
```
### findKey
the `findKey` function returns where a key is in a file.

usage:
``` python
findKey("/path/to/file.vsml", "ExampleKey1", "ExampleSection1") # returned: 1
```
### readKeyValue
the `readKeyValue` function returns the value of a key.

usage:
``` python
readKeyValue("/path/to/file.vsml", "ExampleKey1", "ExampleSection1") # returned: "testValue1"
```
### editKeyValue
the `editKeyValue` function changes the value of a key.

usage:
``` python
editKeyValue("/path/to/file.vsml", "ExampleKey1", "NotExampleValue1", "ExampleSection1")
```
### rename
the `rename` function changes the name of a key, or a section.

usage (key):
``` python
rename("/path/to/file.vsml", "NotExampleKey1", "ExampleSection1", key="ExampleKey1")
```
usage (section):
``` python
rename("/path/to/file.vsml", "NotExampleSection1", "ExampleSection1")
```
### add
the `add` function adds a key, or section.

usage (key, by section):
``` python
add("/path/to/file.vsml", section="ExampleSection1", key="ExampleKey2", value="ExampleValue2")
```
usage (key, by line number):
``` python
add("/path/to/file.vsml", lineNum=27, key="ExampleKey2", value="ExampleValue2")
```
usage (section, add to end of file):
``` python
add("/path/to/file.vsml", section="ExampleSection2")
```
usage (section, by line number):
``` python
add("/path/to/file.vsml", lineNum=26, section="ExampleSection2")
```
### delete
the `delete` function deletes a key, or section.

usage (key):
``` python
delete("/path/to/file.vsml", section="ExampleSection1", key="ExampleKey1")
```
usage (section):
``` python
delete("/path/to/file.vsml", section="ExampleSection1")
```
usage (line number):
``` python
delete("/path/to/file.vsml", lineNum=27)
```
