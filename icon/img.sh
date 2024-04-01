#!/bin/bash

IMAGES_DIR=$1
CURRENT_DIR=$(basename "$1")
OUTPUT_FILE=$1"/img.json"

# 获取图片名称列表
# image_names=($(find $IMAGES_DIR -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg"\) -exec basename {} \;))
image_name=($(find $IMAGES_DIR -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg" \) -exec basename {} \;))
image_names=($(printf "%s\n" "${image_name[@]}" | sort -n))

# 输出到json文件
echo "{" > $OUTPUT_FILE
echo '  "name": "'${CURRENT_DIR}'",' >> $OUTPUT_FILE
echo '  "description": "Made by BgCode",' >> $OUTPUT_FILE
echo '  "icons": [' >> $OUTPUT_FILE
for ((i=0; i<${#image_names[@]}; i++)); do
  echo '    {' >> $OUTPUT_FILE
  echo '      "name": "'${image_names[i]}'",'         >> $OUTPUT_FILE
  echo '      "url": "https://cdn.jsdelivr.net/gh/bgvioletsky/QX/icon/'${CURRENT_DIR}'/'${image_names[i]}'"' >> $OUTPUT_FILE
  if [ $i -ne $((${#image_names[@]}-1)) ]; then
    echo '    },' >> $OUTPUT_FILE
  else
    echo '    }' >> $OUTPUT_FILE
  fi
done
echo '  ]' >> $OUTPUT_FILE
echo "}" >> $OUTPUT_FILE