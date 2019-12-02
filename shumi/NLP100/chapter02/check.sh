# 10
wc -l < hightemp.txt

# 11
diff -u <(python 11.py) <(cat hightemp.txt | tr '\t' ' ')

# 12
diff -u col1.txt  <(cut -f1 hightemp.txt)
diff -u col2.txt  <(cut -f2 hightemp.txt)

# 13
diff -u merge_col.txt <(paste col1.txt col2.txt)

# 14
diff -u <(python 14.py) <(head -n 10 hightemp.txt)

# 15
diff -u <(python 15.py) <(tail -n 10 hightemp.txt)

# 16
N=$(wc -l < hightemp.txt)
split_num=5
split_page_num=$((N / 5))
if test $((N % split_num)) -ne 0
then
    split_page_num=$((split_page_num + 1))
fi
split -l $((split_page_num)) -d hightemp.txt hightemp_bash_split

for i in `seq -w 0`
do
    diff -u "split_hightemp${i}.txt" "hightemp_bash_split${i}.txt"
done

# 17
sort -u col1.txt
echo ""
python 17.py
# pythonのsortは文字コード順に並ぶため同じように並べるのは難しい
#diff -u <(python 17.py) <(sort -u col1.txt)

# 18
sort -k 3r,3 hightemp.txt
echo ""
python 18.py

# 19
echo ""
cut -f1 hightemp.txt | sort | uniq -c | sort -r | cut -f2
echo ""
python 19.py