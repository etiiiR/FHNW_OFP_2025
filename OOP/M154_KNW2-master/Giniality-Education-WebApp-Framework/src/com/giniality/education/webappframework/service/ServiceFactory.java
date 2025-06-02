package com.giniality.education.webappframework.service;

import java.util.Map;

/**
 * Factory for creating service request objects.
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
public class ServiceFactory {

	/**
	 * Static instance of this registry -> Singleton.
	 */
	private static ServiceFactory _instance = new ServiceFactory();

	/**
	 * Gets the instance of this registry.
	 * 
	 * @return The instance.
	 */
	public static ServiceFactory getInstance() {
		return _instance;
	}

	/**
	 * Constructor not visible. Use <code>getInstance</code> 
	 * method to receive an instance of this registry.
	 */
	private ServiceFactory() {
		super();
	}

	/**
	 * Creator.
	 * 
	 * @return The created service request.
	 */
	public ServiceRequest createDefaultServiceRequest() {
		return new UCDefaultServiceRequest();
	}
	
	/**
	 * Creator.
	 * 
	 * @param inRequestParamMap The map containing request parameters.
	 * 
	 * @return The created service request.
	 */
	public ServiceRequest createServiceRequest(Map inRequestParamMap) {
		return new UCServiceRequest(inRequestParamMap);
	}
}