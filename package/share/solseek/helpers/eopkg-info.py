#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys
import os
import lzma

def generate_cache(index_path):
    if os.path.isfile(index_path):
        actual_path = index_path
    elif os.path.isfile(index_path + ".xz"):
        actual_path = index_path + ".xz"
    else:
        print(f"Error: Could not find index file at '{index_path}'", file=sys.stderr)
        return False

    if actual_path.endswith('.xz'):
        f = lzma.open(actual_path, 'rb')
    else:
        f = open(actual_path, 'rb')

    try:
        # We capture both 'start' and 'end' events to safely clear the root.
        # This guarantees memory stays strictly flat (O(1)) even for massive files.
        context = ET.iterparse(f, events=('start', 'end'))
        context = iter(context)
        event, root = next(context)

        for event, elem in context:
            if event == 'end' and elem.tag == 'Package':
                name_elem = elem.find('Name')
                if name_elem is not None and name_elem.text:
                    pkg_name = name_elem.text

                    # --- Extract Version & Release ---
                    version = "Unknown"
                    release = "Unknown"
                    history = elem.find('History')
                    if history is not None:
                        updates = history.findall('Update')
                        if updates:
                            try:
                                latest_update = max(updates, key=lambda u: int(u.get('release', 0)))
                            except ValueError:
                                latest_update = updates[0]

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

                    # --- Output Generation for Awk Cache ---

                    # 1. The invisible ID header for awk to match against
                    print(f"ID:{pkg_name}")

                    # 2. Formatted ANSI output
                    print(f"\033[1;34mName:\033[0m {pkg_name}")
                    print(f"\033[1;34mVersion:\033[0m {version} (Release: {release})")
                    print(f"\033[1;34mSummary:\033[0m {summary.strip()}")
                    print(f"\033[1;34mLicense:\033[0m {', '.join(licenses) if licenses else 'None'}")
                    print(f"\n\033[1;34mDescription:\033[0m\n{description.strip()}")

                    print("\n\033[1;34mDependencies:\033[0m")
                    if deps:
                        for dep in deps:
                            print(f"  - {dep}")
                    else:
                        print("  None")

                    # 3. Print the ASCII Record Separator (\x1e) to close the block
                    print("\x1e", end="")

                # Clear the element and root to prevent memory leaks during iteration
                elem.clear()
                root.clear()

    except Exception as e:
        print(f"Error parsing XML: {e}", file=sys.stderr)
        return False
    finally:
        f.close()

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_cache.py <xml_path> > /tmp/solseek_cache.txt", file=sys.stderr)
        sys.exit(1)

    index_path = sys.argv[1]
    generate_cache(index_path)
