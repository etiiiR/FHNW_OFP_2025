package com.giniality.education.webappframework.service;

import java.util.Iterator;

/**
 * This interface defines a simple request which
 * contains several parameters being stored using
 * a key.
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
public interface ServiceRequest {

	/**
	 * Getter.
	 * 
	 * @param inParameterName The name of the parameter to get.
	 * 
	 * @return The parameter as string or null if it has not been found.
	 */
	public String getParameter(String inParameterName);
	
	/**
	 * Getter.
	 * 
	 * @return The list iterator containing all parameter names.
	 */
	public Iterator getParameterNames();
	
	/**
	 * Getter.
	 * 
	 * @return The list iterator containing all parameter values.
	 */
	public Iterator getParameterValues();
}
