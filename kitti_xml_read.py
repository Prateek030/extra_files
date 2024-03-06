import xml.etree.ElementTree as ET

def read_kitti_ground_truth(xml_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through objects in the XML file
    for obj in root.findall('object'):
        obj_type = obj.find('name').text
        truncated = int(obj.find('truncated').text)
        difficult = int(obj.find('difficult').text)

        # Bounding box coordinates
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        # Print or process the information as needed
        print(f"Object Type: {obj_type}, Truncated: {truncated}, Difficult: {difficult}")
        print(f"Bbox: xmin={xmin}, ymin={ymin}, xmax={xmax}, ymax={ymax}")

# Replace 'path/to/your/tracklet_labels.xml' with the actual path to your tracklet_labels.xml file
xml_file_path = 'path/to/your/tracklet_labels.xml'

# Read KITTI ground truth XML
read_kitti_ground_truth(xml_file_path)
