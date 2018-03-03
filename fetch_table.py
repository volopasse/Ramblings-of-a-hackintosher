import plistlib, urllib

# Read the plist data from this url
url = "https://gfe.nvidia.com/mac-update"
data = urllib.urlopen(url).read()
plist = plistlib.readPlistFromString(data)

# HTML table formatting
table = "<table><tr><th>Build</th><th>OS</th><th>Size</th><th>URL</th></tr>"

def get_version(build):
    # This works for 10.8 and above
    version = int(build[:2]) - 4
    
    # This is for finding the point update
    # A = .1, B = .2, C = .3 etc..
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    point_update = alphabet.find(build[2].lower())

    # After 10.11 it got renamed to macOS (little detail :D)
    if version > 11:
        version = "macOS 10.{}.{} ({})".format(version, point_update, build)
    else:
        version = "Mac OS X 10.{}.{} ({})".format(version, point_update, build)

    return version

def get_megabytes(_bytes):
    return int(_bytes)/1048576

# HTML formatting
for update in plist["updates"]:
    new_html = "<tr></tr>"
    
    # Get the macOS/Mac OS X version + point update
    update["OS"] = get_version(update["OS"])
    
    # Convert bytes to mega bytes
    update["size"] = "{} MB".format(get_megabytes(update["size"]))
    
    # Append a table row
    table_row = "<tr>"
    
    # Add build number
    table_row += "<td>{}</td>".format(update["version"])
    
    # Add macOS/Mac OS X version
    table_row += "<td>{}</td>".format(update["OS"])
    
    # Add size in MB
    table_row += "<td>{}</td>".format(update["size"])
    
    # Add download link
    table_row += "<td><a href=\"{}\">Download</a></td>".format(update["downloadURL"])

    # End table row
    table_row += "</tr>"
    table += table_row

# Add a footer
footer = "<br><br><footer>Made by Gijs - <a href=\"https://github.com/bisquitue/\">Github</a></footer>"

# End table
table += "</table>"

print(table + footer)
