/**
 * This CustomerReadService implements a model (Service) by using Giniality´s WebApp-Framework.
 */

package ch.ilv.crm.webclient.services;

import com.giniality.education.webappframework.service.Service;
import com.giniality.education.webappframework.service.ServiceRequest;

import ch.ilv.crm.business.CustomerFactory;
import ch.ilv.crm.business.ICustomer;

public class CustomerReadService implements Service {
	
	// The customer factory
	private CustomerFactory theCustomerFactory = null;
	
	/**
	 * For informations look at this framework in:
	 * @see com.giniality.education.webappframework.service.Service#process(com.giniality.education.webappframework.service.ServiceRequest)
	 */
	public Object process(ServiceRequest inRequest) {
		
		ICustomer result = null;
		
		// Get the text from the inputfield and send it to the view
		String customerIdString = inRequest.getParameter("customerId");
		
		// Variable declaration
		int customerId = Integer.parseInt(customerIdString);

		// Get the Instance of the CustomerFactory
		theCustomerFactory = CustomerFactory.getInstance();
		
		// Select the customer by the customerID
		result = theCustomerFactory.findCustomer(customerId);
		
		return result;
	}

	/**
	 * For informations look at this framework in:
	 * @see com.giniality.education.webappframework.service.Service#getAliasName()
	 */
	public String getAliasName() {
		return "ReadCustomerService";
	}
}
