package TotalVideosByCategory;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class TotalVideosByCategoryReducer extends Reducer<IntWritable, IntWritable, IntWritable, IntWritable> {
    private IntWritable totalVideos = new IntWritable();

    @Override
    protected void reduce(IntWritable category, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        int count = 0;

        for (IntWritable value : values) {
            count += value.get();
        }

        totalVideos.set(count);
        context.write(category, totalVideos);
    }
}
