package Top_50_FavoriteVideo;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class Top50FavoriteVideosReducer extends Reducer<IntWritable, Text, Text, IntWritable> {
    private int count = 0;

    @Override
    protected void reduce(IntWritable likeCount, Iterable<Text> videos, Context context) throws IOException, InterruptedException {
        for (Text videoId : videos) {
            if (count < 50) {
                // Emit the top 50 favorite videos
                context.write(videoId, likeCount);
                count++;
            } else {
                break;  // Stop after emitting the top 50
            }
        }
    }
}
