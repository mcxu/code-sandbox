package util;

import java.io.File;

public class FileUtils {
    public void printFileSystem() {
        File file = new File(".");
        for (String fileNames : file.list()) {
            System.out.println(fileNames);
        }
    }
}
