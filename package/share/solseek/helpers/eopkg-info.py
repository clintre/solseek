#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys
import os
import lzma

def get_pkg_info(index_path, target_pkg):
    # Determine if the file is compressed or raw XML
    if os.path.isfile(index_path):
        actual_path = index_path
    elif os.path.isfile(index_path + ".xz"):
        actual_path = index_path + ".xz"
    else:
        print(f"Error: Could not find index file at '{index_path}'")
        return False

    # Open the file transparently
    if actual_path.endswith('.xz'):
        f = lzma.open(actual_path, 'rb')
    else:
        f = open(actual_path, 'rb')

    try:
        context = ET.iterparse(f, events=('end',))
        
        for event, elem in context:
            if elem.tag == 'Package':
                name_elem = elem.find('Name')
                if name_elem is not None and name_elem.text == target_pkg:
                    
                    # --- Extract Version & Release ---
                    version = "Unknown"
                    release = "Unknown"
                    history = elem.find('History')
                    if history is not None:
                        updates = history.findall('Update')
                        if updates:
                            # Safely find the update with the highest release number
                            try:
                                latest_update = max(updates, key=lambda u: int(u.get('release', 0)))
                            except ValueError:
                                latest_update = updates[0] # Fallback if release isn't an integer
                                
                            version = latest_update.findtext('Version', default='Unknown')
                            release = latest_update.get('release', 'Unknown')

                    # Extract Standard Data
                    summary = elem.findtext('Summary', default='No summary available')
                    description = elem.findtext('Description', default='No description available')
                    licenses = [lic.text for lic in elem.findall('License') if lic.text]
                    
                    deps = []
                    runtime_deps = elem.find('RuntimeDependencies')
                    if runtime_deps is not None:
                        deps = [dep.text for dep in runtime_deps.findall('Dependency') if dep.text]
                    
                    # Formatted ANSI output
                    print(f"\033[1;34mName:\033[0m {target_pkg}")
                    print(f"\033[1;34mVersion:\033[0m {version} (Release: {release})\033[0m")
                    print(f"\033[1;34mSummary:\033[0m {summary.strip()}")
                    print(f"\033[1;34mLicense:\033[0m {', '.join(licenses) if licenses else 'None'}")
                    print(f"\n\033[1;34mDescription:\033[0m\n{description.strip()}")
                    
                    print("\n\033[1;34mDependencies:\033[0m")
                    if deps:
                        for dep in deps:
                            print(f"  - {dep}")
                    else:
                        print("  None")
                        
                    elem.clear()
                    f.close()
                    return True
                
                # Clear the element from memory if it's not the package
                elem.clear()
    except Exception as e:
        print(f"Error parsing XML: {e}")
    finally:
        f.close()
        
    return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: eopkg-info.py <xml_path> <package_name>")
        sys.exit(1)
        
    index_path = sys.argv[1]
    target_pkg = sys.argv[2]
    
    if not get_pkg_info(index_path, target_pkg):
        print(f"Not Found")
