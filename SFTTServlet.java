import org.json.*;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;
import java.util.ArrayList;
import java.util.Arrays;


@WebServlet("/loan-calculator")
public class  SFTTServlet extends HttpServlet {
    Connection connection;
    PreparedStatement find;

    public void init(ServletConfig config) {
        try {


            Class.forName("com.mysql.jdbc.Driver");
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/reaction?user=stewie3540&password=root");
            //addressBook = connection.prepareStatement("insert into person(firstname,lastname,address,phone) values (?, ? , ? , ? )");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException {
        String sts = "";
        String inputString = request.getParameter("num");
        try {
            JSONObject inputValues = new JSONObject(inputString);
            double[] array = new double[5];
            String val;
            val = inputValues.getString("one");

            String query = "SELECT *  from CR_MP_CR_MP_CR_HK LIMIT 10";

            Arrays.sort(array);

            String yes = "yes";
            find = connection.prepareStatement(query);
            ResultSet result = find.executeQuery();
	   
            String num = null;
            String num2= null;

	    ArrayList<String>  test= new ArrayList<String>();
	    ArrayList<String>  test2= new ArrayList<String>();
	    ArrayList<String>  test3= new ArrayList<String>();
            while (result.next()) {

		test.add(result.getString(val));
		test2.add(result.getString("TIMING"));
                test3.add(result.getString("CR_HK"));               
            }
		JSONObject jsn = new JSONObject();
            	jsn.put("sum", test);
		jsn.put("time",test2);
		jsn.put("crlp",test3);
		
                 PrintWriter out = response.getWriter();
           	 out.println(jsn);


        } catch (Exception e) {
            System.out.println("Servlet died");
            e.printStackTrace();
        }
        PrintWriter out = response.getWriter();
        out.println(sts);
    }

    @Override
    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
}

