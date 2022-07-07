public class videoMain {
    public static void main(String[]args){

        VideoClip clip1 = new VideoClip("clip1");
        VideoClip clip2 = new VideoClip("clip2");
        VideoClip clip3 = new VideoClip("clip3");
        VideoClip clip4 = new VideoClip("clip4");

        videoManager vm = videoManager.getInstance();

        vm.addVideo(clip1);
        vm.addVideo(clip4);

        videoManager vm2 = videoManager.getInstance();
        vm2.addVideo(clip2);
        vm2.addVideo(clip3);

        System.out.println(vm.videoClip.size());
        System.out.println(vm2.videoClip.size());

        vm.deleteVideo(clip1);
        vm2.deleteVideo(clip3);

        System.out.println(vm.videoClip.size());
        System.out.println(vm2.videoClip.size());
    }
    
}
