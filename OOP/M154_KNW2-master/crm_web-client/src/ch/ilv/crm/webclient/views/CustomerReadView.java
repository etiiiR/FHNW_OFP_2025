/**
 * This CustomerReadView implements a view by using Giniality´s WebApp-Framework.
 */

package ch.ilv.crm.webclient.views;

import com.giniality.education.webappframework.view.AbstractHtmlView;

import ch.ilv.crm.business.ICustomer;

public class CustomerReadView extends AbstractHtmlView {
		
	/**
	 * For informations look at this framework in:
	 * @see com.giniality.education.webappframework.view.AbstractHtmlView#createPageContents()
	 * 
	 * @return text The text which is shown on the website
	 */
	public String createPageContents() {
		
		String text = "";
		
		Object displayObject = getDisplayObject();
		
		if (displayObject != null) {
			ICustomer selectedCustomer = (ICustomer)displayObject;
			text = "<h1>Der gesuchte Kunde wurde erfolgreich gefunden</h1>";
			text += "<h3>Name: " + selectedCustomer.getName() + "<br />\n Vorname: " + selectedCustomer.getForename() + "</h3>";
		} else {
			text = "<h1>Der Kunde wurde nicht gefunden!</h1>";
		}
		
		return text;
	}

	/**
	 * For informations look at this framework in:
	 * @see com.giniality.education.webappframework.view.AbstractHtmlView#getTitle()
	 */
	public String getTitle() {
		return "crm-app";
	}

	/**
	 * For informations look at this framework in:
	 * @see com.giniality.education.webappframework.view.AbstractHtmlView#getAliasName()
	 */
	public String getAliasName() {
		return "ReadCustomerView";
	}
}
