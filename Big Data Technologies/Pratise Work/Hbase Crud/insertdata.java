package createHbase;

import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.ConnectionFactory;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Table;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.hbase.client.Delete;

public class insertdata {
	
public static void main(String[] args) throws IOException {
	
Configuration conf = HBaseConfiguration.create();
Connection connection = ConnectionFactory.createConnection(conf);
Table table = connection.getTable(TableName.valueOf("emp1"));
try {
Put put1 = new Put(Bytes.toBytes("row1"));
Put put2 = new Put(Bytes.toBytes("row2"));
Put put3 = new Put(Bytes.toBytes("row3"));

// add the data in HBase table
put1.addColumn(Bytes.toBytes("education"), Bytes.toBytes("Type"),Bytes.toBytes("Regular"));
put2.addColumn(Bytes.toBytes("education"), Bytes.toBytes("Course"),Bytes.toBytes("MCA"));
put3.addColumn(Bytes.toBytes("education"), Bytes.toBytes("Duration"),Bytes.toBytes("02 years"));
put1.addColumn(Bytes.toBytes("post"), Bytes.toBytes("Technical"),Bytes.toBytes("Java"));
put2.addColumn(Bytes.toBytes("post"), Bytes.toBytes("Department"),Bytes.toBytes("MMG"));
put3.addColumn(Bytes.toBytes("post"), Bytes.toBytes("Salary"),Bytes.toBytes("50000"));
table.put(put1);
table.put(put2);
table.put(put3);

System.out.print("Operation Done");
} 

finally 
{
table.close();
connection.close();
}
}
}