import java.awt.Image;

/**
 * Proxy class for video clip
 * @author Ava Reese
 * @author Katherine Butt
 */
public class VideoClip{

    public Image previewImg;

    public int startFrame; //starting frame
    public int endFrame; //ending frame

    public float fps; //frames per second

    public String videoFileName; //filename
    public String videoDescription; //file description


    /** empty construtor for video clip */
    public VideoClip(){}


    /** constructor which holds a string value for videoName */ 
    public VideoClip(String videoName){
        this.videoFileName = videoName;

    }


}