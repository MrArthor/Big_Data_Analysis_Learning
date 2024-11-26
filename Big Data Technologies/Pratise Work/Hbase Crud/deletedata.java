package createHbase;



import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Delete;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.hbase.client.Result;


public class deletedata{
	
public static void main(String args[])throws IOException{
	
Configuration config = HBaseConfiguration.create();
HTable table=new HTable(config, "emp1");
Delete del=new Delete(Bytes.toBytes("row1"));
del.deleteColumns(Bytes.toBytes("education"),Bytes.toBytes("Type") );
table.delete(del);
System.out.println("value-delted");
table.close();
}
}