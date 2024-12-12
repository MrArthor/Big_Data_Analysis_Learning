package createHbase;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.*;
import java.io.IOException;


public class createTable
{
	public static void main(String [] args) throws IOException{
		Configuration conf = HBaseConfiguration.create();
		Connection con = ConnectionFactory.createConnection(conf);
		Admin ad = con.getAdmin();
		HTableDescriptor ht = new HTableDescriptor(TableName.valueOf("emp2"));
		ht.addFamily(new HColumnDescriptor("education"));
		ht.addFamily(new HColumnDescriptor("post"));
	if(!ad.tableExists(ht.getTableName()))
	{
		System.out.println("Creating table");
		ad.createTable(ht);
		System.out.println("Done");
		
	}
	}
	
}