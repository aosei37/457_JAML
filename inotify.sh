#!/bin/bash


watchedDir="/home/bossqwea/ENEE457/inotify_dir"

inotifywait \
  --monitor "$watchedDir" \
  --exclude '\.swp|\.swx' \
  -e create \
  -e delete \
  -e modify \
  -e move \
  --timefmt '%Y-%m-%dT%H:%M:%S' \
  --format '%T %w %f %e' \
| while read datetime dir filename event; do
  	name=$(stat --format %U $filename 2>/dev/null)
 	  echo -e "DATE: $datetime -- USER: $name -- FILE:$dir$filename -- EVENT: $event" >> watch.log
done
