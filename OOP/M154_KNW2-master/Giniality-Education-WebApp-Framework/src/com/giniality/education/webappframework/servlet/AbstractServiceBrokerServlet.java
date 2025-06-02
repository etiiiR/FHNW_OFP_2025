package com.giniality.education.webappframework.servlet;

import java.io.IOException;
import java.io.OutputStreamWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.giniality.education.webappframework.registry.ServiceRegistry;
import com.giniality.education.webappframework.registry.ViewRegistry;
import com.giniality.education.webappframework.service.Service;
import com.giniality.education.webappframework.service.ServiceFactory;
import com.giniality.education.webappframework.service.ServiceRequest;
import com.giniality.education.webappframework.view.ServiceNotFoundView;
import com.giniality.education.webappframework.view.View;
import com.giniality.education.webappframework.view.ViewNotFoundView;

/**
 * This <code>Servlet</code> can handle requests for a <code>Service</code> 
 * and for a <code>View</code>. Additional parameters will automatically
 * routed to the selected <code>Service</code>.
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
public abstract class AbstractServiceBrokerServlet extends HttpServlet {

	/**
	 * Constant defining the serial version UID.
	 */
	private static final long serialVersionUID = 1L;

	/**
	 * Constant defining the service parameter.
	 */
	public final static String SERVICE_PARAMETER = "service";

	/**
	 * Constant defining the view parameter.
	 */
	public final static String VIEW_PARAMETER = "view";

	/**
	 * Initializes the registration of <code>Service</code>s and
	 * <code>View</code>s. 
	 * 
	 * Implement this method in a subclass in oder to register 
	 * <code>Service</code> and <code>View</code> implementations 
	 * that are part of your application.
	 */
	protected abstract void initRegistry();

	public void init() {
		ViewRegistry.getInstance().registerView(new ViewNotFoundView());
		initRegistry();
	}

	/**
	 * Processes an incoming request from a browser. At this point we
	 * have to check which <code>Service</code> and which <code>View</code> 
	 * the user wants to start.
	 * The <code>Service</code> parameter is optional (depending on the 
	 * <code>View</code> to be displayed). If no <code>View</code> has 
	 * been specified, an error page will be shown.
	 * 
	 * @param inRequest The incoming request.
	 * @param inResponse The outgoing response.
	 * 
	 * @throws IOException
	 * @throws ServletException
	 */
	public void service(
		HttpServletRequest inRequest,
		HttpServletResponse inResponse)
		throws ServletException, IOException {

		// get parameter we need
		String aServiceName = inRequest.getParameter(SERVICE_PARAMETER);
		String aViewName = inRequest.getParameter(VIEW_PARAMETER);

		// SERVICE
		Object aResult = null;
		if (aServiceName != null && aServiceName.length() > 0) {
			// remove whitespaces
			aServiceName = aServiceName.trim();

			// find service in registry
			Service aServiceObject =
				ServiceRegistry.getInstance().findService(aServiceName);

			// create neutral request object
			ServiceRequest aRequest =
				ServiceFactory.getInstance().createServiceRequest(
					inRequest.getParameterMap());

			// process service with incoming request
			if (aServiceObject != null) {
				aResult = aServiceObject.process(aRequest);
			} else {

				// create error view
				View anErrorView = new ServiceNotFoundView();
				anErrorView.setDisplayObject(inRequest);
				sendResponse(inResponse, anErrorView);
			} // else
		}

		// VIEW
		// find in registry
		View aViewObject = ViewRegistry.getInstance().findView(aViewName);
		if (aViewObject != null) {
			// set display object on view
			aViewObject.setDisplayObject(aResult);
			
			sendResponse(inResponse, aViewObject);
		} else { // -> no display view registered under given alias name
			// create and show error view
			aViewObject = new ViewNotFoundView();

			// set failed request as display object
			aViewObject.setDisplayObject(inRequest);

			sendResponse(inResponse, aViewObject);
		} // else
	}

	/**
	 * Sends a view as response back to the client.
	 * 
	 * @param inResponse The response we can write into.
	 * @param inView The view that should be "displayed".
	 * 
	 * @throws IOException Indicating that the response could not be send
	 * 					    for some reason.
	 */
	private void sendResponse(HttpServletResponse inResponse, View inView)
		throws IOException {

		// OUTPUT
		// get output stream writer
		OutputStreamWriter aResponseStreamWriter =
			new OutputStreamWriter(inResponse.getOutputStream());

		// dump view to writer
		aResponseStreamWriter.write(inView.show());

		// force data to be sent back to client
		aResponseStreamWriter.flush();
	}
}