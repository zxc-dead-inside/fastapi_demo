docker-compose up

## SQL решение
```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE SPLIT_PART(full_names.name,'.', 1) = short_names.name;
```

###Если возможно имя файла с точкой (filneme.123.json) 
```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE LEFT(full_names.name, LENGTH(full_names.name) - POSITION('.' IN REVERSE(full_names.name))) = short_names.name;
```
