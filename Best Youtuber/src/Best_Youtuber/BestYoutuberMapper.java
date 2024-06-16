package Best_Youtuber;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class BestYoutuberMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private Text channelTitle = new Text();
    private final static IntWritable one = new IntWritable(1);

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String[] columns = value.toString().split("\t");
        if (columns.length == 12) {
            channelTitle.set(columns[3]);
            context.write(channelTitle, one);
        }
    }
}
