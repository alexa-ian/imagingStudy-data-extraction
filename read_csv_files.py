import csv
from collections import defaultdict

def read_csv_files(input_files, output_file):
    sum_per_value = defaultdict(int)
    
    unique_values = set()

    for file in input_files:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
                       
            for row in reader:
                value = row[1]
                amount = int(row[2])
                
                sum_per_value[value] += amount
                
                unique_values.add(value)

    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        
        writer.writerow(['BodySite', 'Sum'])
        
        for value in sorted(unique_values):
            writer.writerow([value, sum_per_value[value]])

input_files = ['./csv-output/result_laterality_L_bodySite_partition_0-1.csv', 
               './csv-output/result_laterality_L_bodySite_partition_2-3.csv',
               './csv-output/result_laterality_L_bodySite_partition_4-5.csv',
               './csv-output/result_laterality_L_bodySite_partition_6-7.csv',
               './csv-output/result_laterality_L_bodySite_partition_8-9.csv',
               './csv-output/result_laterality_L_bodySite_partition_10-11.csv'
               ]
output_file = './output_laterality_L_bodySite.csv'
read_csv_files(input_files, output_file)
