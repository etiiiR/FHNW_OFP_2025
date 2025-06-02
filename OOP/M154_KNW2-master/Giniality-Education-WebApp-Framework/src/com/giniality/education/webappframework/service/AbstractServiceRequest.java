/*
 * Created on 27.01.2004
 *
 * To change the template for this generated file go to
 * Window&gt;Preferences&gt;Java&gt;Code Generation&gt;Code and Comments
 */
package com.giniality.education.webappframework.service;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * @author Administrator
 *
 * To change the template for this generated type comment go to
 * Window&gt;Preferences&gt;Java&gt;Code Generation&gt;Code and Comments
 */
abstract class AbstractServiceRequest implements ServiceRequest {

	/**
	 * The parameters.
	 */
	protected Map parameters;

	/**
	 * Default constructor initializing mandatory fields.
	 */
	protected AbstractServiceRequest() {
		super();

		// init
		parameters = new HashMap();
	}

	/**
	 * @see com.giniality.education.webappframework.service.ServiceRequest#getParameter(java.lang.String)
	 */
	public String getParameter(String inParameterName) {
		return (String) parameters.get(inParameterName);
	}

	/**
	 * @see com.giniality.education.webappframework.service.ServiceRequest#getParameterNames()
	 */
	public Iterator getParameterNames() {
		return parameters.keySet().iterator();
	}

	/**
	 * @see com.giniality.education.webappframework.service.ServiceRequest#getParameterValues()
	 */
	public Iterator getParameterValues() {
		return parameters.values().iterator();
	}
}
