import xml.etree.ElementTree as ET
import json

def parse_tracklet_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    tracklet_data = {}
    
    for item in root.findall('.//item'):
        object_type_elem = item.find('objectType')
        if object_type_elem is not None:
            object_type = object_type_elem.text
            poses = []

            for pose in item.findall('.//item'):
                pose_data = {
                    'tx': float(pose.find('tx').text) if pose.find('tx') is not None else 0.0,
                    'ty': float(pose.find('ty').text) if pose.find('ty') is not None else 0.0,
                    'tz': float(pose.find('tz').text) if pose.find('tz') is not None else 0.0,
                    'rx': float(pose.find('rx').text) if pose.find('rx') is not None else 0.0,
                    'ry': float(pose.find('ry').text) if pose.find('ry') is not None else 0.0,
                    'rz': float(pose.find('rz').text) if pose.find('rz') is not None else 0.0,
                    'state': int(pose.find('state').text) if pose.find('state') is not None else 0,
                    'occlusion': int(pose.find('occlusion').text) if pose.find('occlusion') is not None else 0,
                    'occlusion_kf': int(pose.find('occlusion_kf').text) if pose.find('occlusion_kf') is not None else 0,
                    'truncation': int(pose.find('truncation').text) if pose.find('truncation') is not None else 0,
                }
                poses.append(pose_data)

            tracklet_data[object_type] = poses

    return tracklet_data

def save_to_json(data, json_file):
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

# Example Usage:
xml_file_path = "/content/tracklet_labels.xml"
json_file_path = "output.json"

tracklet_data = parse_tracklet_xml(xml_file_path)
if tracklet_data:
    save_to_json(tracklet_data, json_file_path)
