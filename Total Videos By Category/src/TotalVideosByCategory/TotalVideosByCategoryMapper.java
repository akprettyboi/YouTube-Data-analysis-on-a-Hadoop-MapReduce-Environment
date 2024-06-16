package TotalVideosByCategory;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class TotalVideosByCategoryMapper extends Mapper<LongWritable, Text, IntWritable, IntWritable> {
    private IntWritable category = new IntWritable(0);
    private final static IntWritable one = new IntWritable(1);

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String[] columns = value.toString().split("\t");
        if (columns.length == 12) {
            category.set(Integer.parseInt(columns[4])); // Assuming Category ID is an integer
            context.write(category, one);
        }
    }
}
