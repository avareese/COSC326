import java.util.ArrayList;
import java.util.Collection;

/**
 * Etude 11 Video Manager 
 * @author Ava Reese
 * @author Katherine Butt
 */


public class videoManager {

    private static videoManager instance = null;
    
    public Collection<VideoClip> videoClip = new ArrayList<>();

    String str;


    /** Private constructor method that only the getInstance method can make an 
     * instance of the class.
     */
    private videoManager(){

    }

    /** creates a new instance if the singleton class
     * @returns new instance of videomanager
     */
    public static videoManager getInstance(){
        if(instance == null){
            instance = new videoManager();
        }
        return instance;
    }

    /** method which adds a video clip to the arraylist */
    public void addVideo(VideoClip v){
        videoClip.add(v);
    }

    /** method which deletes a video clip from the arraylist */
    public void deleteVideo(VideoClip v){
        videoClip.remove(v);

    }
    
}
