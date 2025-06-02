package com.giniality.education.webappframework.view;

import javax.servlet.http.HttpServletRequest;

/**
 * <code>View</code> showing an error page when a <code>View</code> 
 * could not be found in the <code>ViewRegistry</code>.
 *  
 * @author Christian Sauer (CSA), Giniality AG
 */
public class ViewNotFoundView extends AbstractHtmlView {

	/**
	 * Shows the error screen.
	 * 
	 * @return The error screen.
	 */
	public String createPageContents() {
		String aPage = "";

		aPage += "<html><header><title>Error ...</title></header>\n";
		aPage += "<body bgcolor=\"#cc0000\" text=\"#ffffff\">\n";
		aPage += "<center>\n";
		aPage += "The origin query was:<b>"
			+ ((HttpServletRequest) getDisplayObject()).getQueryString()
			+ "</b>\n";
		aPage += "<p>\n";
		aPage
			+= "<h2>The <i>View</i> you have specified is not registered in the <i>ViewRegistry</i>!</h2>\n";
		aPage += "</center></p>\n";
		aPage += "</body>\n";
		aPage += "</html>";

		return aPage;
	}
	
	/**
	 * Gets the title of this page.
	 * 
	 * @return The title of this page.
	 */
	public String getTitle() {
		return "An errot ocurred ...";
	}
	
	/**
	 * Gets the alias name of this page which will be
	 * used in forming urls.
	 * 
	 * @return The alias name of this page.
	 */
	public String getAliasName() {
		return "viewNotFound";
	}
}