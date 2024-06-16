package Max_Rating;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class MaxRatingReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable maxRating = new IntWritable();
    private IntWritable totalRating = new IntWritable();
    private IntWritable totalCommentCount = new IntWritable();

    @Override
    protected void reduce(Text videoId, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int max = Integer.MIN_VALUE;
        int totalRatingValue = 0;
        int totalCommentValue = 0;

        for (IntWritable value : values) {
            int currentValue = value.get();
            if (currentValue > max) {
                max = currentValue;
            }
            if (currentValue >= 0) {
                totalRatingValue += currentValue;
            } else {
                totalCommentValue += currentValue;
            }
        }

        maxRating.set(max);
        totalRating.set(totalRatingValue);
        totalCommentCount.set(-totalCommentValue); // Convert back to positive

        // Emit (Video ID, Max Rating)
        context.write(videoId, maxRating);

        // Emit (Video ID, Total Rating)
        context.write(videoId, totalRating);

        // Emit (Video ID, Total Comment Count)
        context.write(videoId, totalCommentCount);
    }
}
