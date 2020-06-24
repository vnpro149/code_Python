# Import modules
import sys
from helper import *

import xml.etree.ElementTree as ET

import xml.dom.minidom as MD

# Main function
if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    # Add print statement here


    #########################################
    #              Procedure 2              #
    #########################################
    print('##################')
    print('###### YAML ######')
    print('##################')

    # Open the user.yaml file as read only

        # Load the stream using safe_load

    # Print the object type
    print("Type of user_yaml variable:")

    print('----------------------')

    # Iterate over the keys of the user_yaml and print them
    print('Keys in user_yaml:')

    print('----------------------')

    # Create a new instance of class User

    # Assign values form the user_yaml to the object user

    # Print the user object
    print('User object:')


    #########################################
    #              Procedure 3              #
    #########################################
    print('##################')
    print('###### JSON ######')
    print('##################')

    # Create JSON structure from the user object
    
    # Print the created JSON structure
    print('Print user_json:')

    print('----------------------')

    # Create JSON structre with indents and soreted keys
    print('JSON with indents and sorted keys')


    #########################################
    #              Procedure 4              #
    #########################################
    print('######################')
    print('# XML - Element Tree #')
    print('######################')

    # Parse the user.xml file

    # Get the root element

    # Print the tags
    print('Tags in the XML:')    

    print('----------------------')

    # Print the value of id tag
    print('id tag value:')

    print('----------------------')

    # Find all elements with the tag address in root

    # Print the adresses in the xml
    print('Addresses:')

    print('----------------------')
    
    # Print the elements in root with their tags and values
    print('Print the structure')    

    # Parsing XML files with MiniDOM 
    print('######################')
    print('### XML - MiniDOM ####')
    print('######################')

    # Parse the user.xml file

    # Print the tags

    print('----------------------')    

    # Accessing element value
    print('Accessing element value')

    print('----------------------')

    # Print elements from the DOM with tag name 'address'
    print('Addresses:')

    print('----------------------')

    # Print the entire structure with printNodes
    print('The structure:')


    #########################################
    #              Procedure 5              #
    #########################################
    print('######################')
    print('#   Use Namespaces   #')
    print('######################')

    # Parse the user.xml file

    # Get the root element

    # Define namespaces 

    # Set table as the root element 

    # Elements in NS a
    print('Elements in NS a:')   

    print('----------------------')

    # Elements in NS b
    print('Elements in NS b:')