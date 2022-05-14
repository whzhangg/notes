# XML file and python xml parsing
### xml file format
xml document is a *string* with the following elements:  
##### Tag
A tag is a construct that begins with `<` and end with `>`. For example, we have *starting tag* as `<section>` , *ending tag* as `</section>`. A tag with no elements is given as `<line />`.
##### Element
An element should *start with a start-tag and end with a matching end-tag*, or consist of an empty tag, the characters between the tags are *elements' content*. It can include other elements, called *child elements*
```html
<greeting>Hello, World!</greeting>
```
##### Attributes
An attributes is a construct that *exists within a start-tag or an empty tag*. For example: `<img src="madonna.jpg" alt="Madonna" />`, which contain two attributes *src* and *alt*.
##### Declaration
xml documents can begin with a *xml declaration* that describes information about themselves, For example: `<?xml version="1.0" encoding="UTF-8"?>`.

### Python parser
reference: https://docs.python.org/3/library/xml.etree.elementtree.html

In python xml file is presented as a tree, `ElementTree` class represents the whole xml documents and `Element` represents a single node in this tree

##### Importing
To importing a xml data file:
```python
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()  # root is an element

# from a string:
root = ET.fromstring() # directly return an element
```

An element has a tag and a dictionary of attributes, for example: `root.tag` and `root.attrib`

##### Iterating
it also has children nodes over which we can iterate:
```python
for child in root:
	print(child.tag, child.attrib)
```

We can also access child by index: `root[0]`

##### Searching
`Element.findall()` finds elements with a tag which are direct children of the current elements

`Element.find()` finds the first child with a given tag

`Element.get()` accesses the elements attributes