package Top_50_FavoriteVideo;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class Top50FavoriteVideosMapper extends Mapper<LongWritable, Text, IntWritable, Text> {
    private IntWritable likes = new IntWritable();
    private Text videoId = new Text();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String[] columns = value.toString().split("\t");
        if (columns.length == 12) {
            videoId.set(columns[0]);
            int likeCount = Integer.parseInt(columns[8]);
            likes.set(likeCount);
            context.write(likes, videoId);
        }
    }
}

