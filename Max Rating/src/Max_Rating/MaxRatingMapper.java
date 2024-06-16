package Max_Rating;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class MaxRatingMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private Text videoId = new Text();
    private IntWritable rating = new IntWritable();
    private IntWritable commentCount = new IntWritable();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String[] columns = value.toString().split("\t");
        if (columns.length == 12) {
            videoId.set(columns[0]);
            int likes = Integer.parseInt(columns[8]);
            int dislikes = Integer.parseInt(columns[9);
            int comments = Integer.parseInt(columns[10]);
            int rating = likes - dislikes;

            // Emit (Video ID, Rating)
            context.write(videoId, new IntWritable(rating));

            // Emit (Video ID, Comment Count)
            context.write(videoId, new IntWritable(comments));
        }
    }
}
