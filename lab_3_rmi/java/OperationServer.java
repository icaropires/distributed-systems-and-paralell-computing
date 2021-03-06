import java.net.MalformedURLException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.rmi.AlreadyBoundException;
import java.rmi.Naming;
import java.rmi.RemoteException;

public class OperationServer {
    public static void main(String[] args) throws RemoteException, AlreadyBoundException, MalformedURLException, UnknownHostException {

		String current_directory = System.getProperty("user.dir");
		System.setProperty("java.security.policy", "file://" + current_directory + "/server.policy");

		if (System.getSecurityManager() == null) {
			System.setSecurityManager(new SecurityManager());
		}

        Operation operation = new example_Operation();

        Naming.rebind("Operation", operation);

		String host = InetAddress.getLocalHost().getHostAddress();
        System.out.println("Object bound to IP "  + host);
    }
}
