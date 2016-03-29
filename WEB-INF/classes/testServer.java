import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;


public class testServer extends HttpServlet{
	Connection connection;
	PreparedStatement find;
	PrintWriter out;
	public void doGet(HttpServletRequest req, HttpServletResponse res)throws IOException, ServletException
	{

		 out = res.getWriter();

		res.setContentType("text/html");
		out.println("<html><body>");
		out.println("<p> hi i like to eat your poo </p>");

		try
		{

			Class.forName("com.mysql.jdbc.Driver");
			connection =  DriverManager.getConnection("jdbc:mysql://localhost:3306/framedata?user=root&password=root");
			

			String query = "SELECT * from STARTUP";

			out.println("<p> your query is: " + query + "</p>");


			find = connection.prepareStatement(query);
           		ResultSet result =  find.executeQuery();
            		int count =0;
           	 while(result.next())
            	{
                	out.println("<p>" + result.getString("CR_MP")
                        + "</p>" );
               		 ++count;
           	 }
           	 out.println("<p>====" + count + "records found ====</p>");
            	out.println("</body></html>");

        } catch (SQLException e) {
		out.println("stack trace:</br>");
           	 e.printStackTrace(out);
		out.println(displayErrorforWeb(e));
        }catch (ClassNotFoundException e){
		e.printStackTrace();
	}


    }
public String displayErrorforWeb(Throwable t)
{
	StringWriter sw = new StringWriter();
	PrintWriter pw = new PrintWriter(sw);
	t.printStackTrace(pw);
	String stackTrace = sw.toString();
	return stackTrace.replace(System.getProperty("line.seperator"),"<br/>\n");
}
  public void destroy() {
        try {
            find.close();

            connection.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }


    }

}
