/**
 * This CRMServlet implements a controller (Servlet) by using Giniality´s WebApp-Framework.
 */

package ch.ilv.crm.webclient.servlet;

import ch.ilv.crm.webclient.services.CustomerCreateService;
import ch.ilv.crm.webclient.services.CustomerReadService;
import ch.ilv.crm.webclient.views.CustomerCreateView;
import ch.ilv.crm.webclient.views.CustomerReadView;

import com.giniality.education.webappframework.registry.ServiceRegistry;
import com.giniality.education.webappframework.registry.ViewRegistry;
import com.giniality.education.webappframework.servlet.AbstractServiceBrokerServlet;

public class CRMServlet extends AbstractServiceBrokerServlet {

	/**
	 * Constant defining the serial version UID.
	 */
	private static final long serialVersionUID = 2L;

	/**
	 * For informations look at this framework in:
	 * @see com.giniality.education.webappframework.servlet.AbstractServiceBrokerServlet#initRegistry()
	 */
	protected void initRegistry() {
		// The Register Views of the customer manager website
		ViewRegistry.getInstance().registerView(new CustomerCreateView());
		ViewRegistry.getInstance().registerView(new CustomerReadView());

		// The Register Services of the customer manager website
		ServiceRegistry.getInstance().registerService(new CustomerCreateService());
		ServiceRegistry.getInstance().registerService(new CustomerReadService());
	}
}