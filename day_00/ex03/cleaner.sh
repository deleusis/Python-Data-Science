#!/bin/sh

if [ -z "$1" ] #если нет входящего файла
  then
    IN_FILE="../ex02/hh_sorted.csv" #то входящий файл этот
  else
    IN_FILE="$1"             
fi

OUT_FILE="hh_positions.csv"

cat $IN_FILE | head -n 1 > $OUT_FILE

cat $IN_FILE | tail -n +2 \
| awk 'BEGIN {FS= OFS= ","}
    {
        if (tolower($3) ~ "junior" && tolower($3) ~ "middle" && tolower($3) ~ "senior")
            $3 = "\"Junior/Middle/Senior\""
        else if (tolower($3) ~ "junior" && tolower($3) ~ "middle")
            $3 = "\"Junior/Middle\""
        else if (tolower($3) ~ "junior" && tolower($3) ~ "senior")
            $3 = "\"Junior/Senior\""
        else if (tolower($3) ~ "middle" && tolower($3) ~ "senior")
            $3 = "\"Middle/Senior\""
        else if (index(tolower($3), "junior"))
            $3 = "\"Junior\""
        else if (index(tolower($3), "middle"))
            $3 = "\"Middle\""
        else if (index(tolower($3), "senior"))
            $3 = "\"Senior\""
        else
            $3 = "\"-\""
        print
    }'\
    >>$OUT_FILE

    # $3 - третье поле